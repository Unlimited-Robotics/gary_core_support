ARG REGISTRY_ENDPOINT
FROM ${REGISTRY_ENDPOINT}/raya.core.base_images.ros_humble:jetsonorin.4.17.beta

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:0


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




# Install Python packages
RUN python3 -m pip install \
    python-can \
    pyserial
