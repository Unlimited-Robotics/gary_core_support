ARG REGISTRY_ENDPOINT
FROM ${REGISTRY_ENDPOINT}/raya.core.base_images.ros_humble:jetsonorin.4.17.beta

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies and Python packages
RUN apt-get update && \
    apt-get install -y \
    python3-pyqt5 \
    ca-certificates \
    curl \
    gnupg \
    lsb-release && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Add Docker’s official GPG key
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up the Docker repository
RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
RUN apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install Python packages
RUN python3 -m pip install \
    python-can==4.2.2 \
    pyserial
