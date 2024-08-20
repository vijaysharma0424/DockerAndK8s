# Multi-stage Dockerfile
# Stage 1: Build the application
FROM maven:3.8.6-eclipse-temurin-17-alpine AS build-stage
WORKDIR /app
COPY pom.xml ./
COPY src ./src

RUN mvn clean package

# Stage 2: Create the runtime image
FROM openjdk:17-jdk-alpine
WORKDIR /app
COPY --from=build-stage /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
