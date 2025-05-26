module.exports = {
    apps: [{
        name: "fastapi-app",
        script: "uvicorn",
        args: "main:app --host 0.0.0.0 --port 8000 --workers 2",
        cwd: __dirname,  // Use __dirname to make path relative to config file
        interpreter: "python",
        instances: 2,
        log_date_format: "YYYY-MM-DD HH:mm Z",
        error_file: "./logs/fastapi-app-error.log",
        out_file: "./logs/fastapi-app-out.log",
        merge_logs: true,
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
// pm2 start main.py -i 2 --name fastapi-app --interpreter python