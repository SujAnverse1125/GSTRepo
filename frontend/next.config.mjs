/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        // This securely proxies requests to your backend without exposing the URL to the browser
        destination: `${process.env.SECRET_BACKEND_URL || 'http://localhost:8000'}/api/:path*`, 
      },
    ]
  },
}

export default nextConfig;
