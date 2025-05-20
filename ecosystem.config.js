module.exports = {
    apps: [{
        name: "fastapi-app",
        script: "uvicorn",
        args: "main:app --host 0.0.0.0 --port 8000 --workers 2",
        cwd: "/home/pitpy/Desktop/trainning/python/fastapi-app",
        interpreter: "/home/pitpy/Desktop/trainning/python/fastapi-app/.venv/bin/python3",  // Update this path to your virtual environment
        instances: 1,
        autorestart: true,
        watch: false,
        max_memory_restart: "1G",
        env: {
            NODE_ENV: "development",
        },
        env_production: {
            NODE_ENV: "production",
        }
    }]
}