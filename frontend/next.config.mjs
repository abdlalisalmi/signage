/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
  images: {
    // loader: "custom",
    remotePatterns: [
      {
        // protocol: "https",
        hostname: "**",
      },
    ],
  },
  engines: {
    node: ">=18.17.0",
  },
};

export default nextConfig;
