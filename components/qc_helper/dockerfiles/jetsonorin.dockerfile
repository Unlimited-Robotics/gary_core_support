ARG REGISTRY_ENDPOINT
FROM ${REGISTRY_ENDPOINT}/raya.core.base_images.ros_humble:jetsonorin.4.17.beta

ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update &&  \
    apt-get install -y python3-pyqt5 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean


RUN python3 -m pip install \
    python-can==4.2.2 \



