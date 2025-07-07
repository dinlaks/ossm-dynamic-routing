# Step 1: Build with Node.js (UBI)
FROM registry.access.redhat.com/ubi8/nodejs-18 AS builder

WORKDIR /opt/app-root/src

# Copy package and lock files
COPY package*.json ./
RUN npm install

# Copy source and build
COPY . .
RUN npm run build

# Step 2: Serve with httpd (UBI)
FROM registry.access.redhat.com/ubi8/httpd-24

# Copy built files into httpd root
COPY --from=builder /opt/app-root/src/dist/ /var/www/html/

# Set correct permissions for OpenShift
RUN chown -R 1001:0 /var/www/html && \
    chmod -R g=u /var/www/html

# Run as non-root OpenShift-compatible UID
USER 1001

EXPOSE 8080

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
