FROM node:18

WORKDIR /app/

# Copy package.json and package-lock.json to the working directory
COPY ./frontend/package*.json .

# Install dependencies using npm
RUN npm install

# Copy the rest of the application code to the working directory
ADD ./frontend .

# Set environment variables
RUN echo "NEXT_PUBLIC_API_URL=/api/v1" > .env
RUN echo "NEXT_PUBLIC_MEDIA_URL=/" >> .env

# Build the application using npm
RUN npm run build

# Expose the port the application runs on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "start"]
