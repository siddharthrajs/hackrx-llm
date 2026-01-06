#!/bin/bash

# HackRx LLM Docker Runner Script

set -e

echo "🚀 Building and running HackRx LLM API..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found!"
    echo "📝 Please create a .env file with your GEMINI_API_KEY"
    echo "💡 Example:"
    echo "   GEMINI_API_KEY=your_api_key_here"
    exit 1
fi

# Build the Docker image
echo "🔨 Building Docker image..."
docker-compose build

# Run the container
echo "🏃 Starting the application..."
docker-compose up -d

# Wait for the application to be healthy
echo "⏳ Waiting for application to be ready..."
sleep 10

# Check if the application is running
if curl -f http://localhost:8000/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo "🌐 API available at: http://localhost:8000"
    echo "📚 API documentation: http://localhost:8000/docs"
    echo ""
    echo "🛑 To stop the application, run: docker-compose down"
else
    echo "❌ Application failed to start properly"
    echo "📋 Check logs with: docker-compose logs"
    exit 1
fi
