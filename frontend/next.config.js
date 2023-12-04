/** @type {import('next').NextConfig} */
const nextConfig = {
 
}

module.exports = {

    images:{
        remotePatterns:[
            {
                protocol: 'https',
                hostname: 'wallspic.com',
                port: '',
                pathname: '/image/**'
            }
        ]
    }
};
