FROM scarolayton/test-2-backend:v1.1 AS backend
FROM scarolayton/test-2-frontend:v1 AS frontend

FROM alpine
RUN apk add --no-cache python3 
# Install system dependencies required by grpcio and other packages
WORKDIR /app 
COPY --from=frontend app/frontend /frontend
COPY --from=backend app/backend/ /backend

# COPY /start_servers.sh /start_servers.sh
# RUN chmod +x /start_servers.sh
CMD ["python", "/backend/manage.py", "runserver"]
# Establece el comando para ejecutar la aplicación completa (Django + Next.js)
