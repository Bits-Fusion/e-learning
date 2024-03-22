/* eslint-disable prettier/prettier */
import { Controller, Headers, Get, Param, Res } from "@nestjs/common";
import { diskStorage } from "multer";
import * as path from 'path';
import fs = require('fs');


export const storage = {
    storage: diskStorage({
        destination: './rooms/Image',
        filename: (req, file, cb) => {
            const filename: string = path.parse(file.originalname).name.replace(/\s/g, '');
            const extension: string = path.parse(file.originalname).ext;
            cb(null, `${filename}${extension}`)
        }
    })

}

@Controller('video')
export class VideoStreamController {
    @Get(':__path')
    async videoStream (@Param('__path') __path: string, @Headers() header: any, @Res() res: any) {
        const range = header.range
        const authHandler = await handelAuth(header);

        if(!authHandler) {
            return res.status(500).send({
                'detail':'There has been internal server error'
            })
        }

        if(authHandler.error) {
            return res.status(401).send({
                'detail':'invalid creadential'
            })
        }

        if(!range){
            return res.status(404).send({
                'detail':'The header do not contain range parameter'
            })
        }

        const videoPath = path.resolve(__dirname, "../../../", `media/music_files/audio/${__path}`);

        if(!fs.existsSync(videoPath)) {
            return res.status(404).send({
                "detail":"The file you are looking for doesn't exist in the database"
            });
        }

        const videoSize = fs.statSync(videoPath).size;
        const CHUNK_SIZE = 1024*1024;
        const _splited = range.replace(/\D/g, ' ').split();
        const start = Number(_splited[0]);
        const end = Math.min(start + CHUNK_SIZE, videoSize - 1);
        

        if(start >= videoSize){
            return res.status(404).send({
                "detail":"Out of range"
            });
        }
        
        const contentLength = end - start + 1;
        const headers = {
            "Content-Range": `bytes ${start}-${end}/${videoSize}`,
            "Accept-Ranges": "bytes",
            "Content-Length": contentLength,
            "Content-Type": "audio/mp3",
        };

        res.writeHead(206, headers);
        const videoStream = fs.createReadStream(videoPath, {
                start:start,
                end:end,
            });

        videoStream.pipe(res);
        return path;
    }
}

const handelAuth = async (header: any) => {
    const containToken: string = await header.authorization;

    if (!containToken){
        return {
            'detail' : 'The Request does not contain Authorization token',
            'error' : true,
        }
    }
    const token = containToken.split(' ')

    const BASE_URL = 'http://localhost:9100/api_root/auth/validate/';

    const Options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            'token': token[1],
        })
    };

    try {
        const message = await fetch(BASE_URL, Options)
        .then((response) => {
            return response.json();
        })
        .catch(error => {
            console.log('error', error);
        })
        return message

    } catch (error) {
        return {
            'detail': error,
            'error': true,
        }
    }

}