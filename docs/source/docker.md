# Docker

Docker is a platform that enables developers to build, deploy, and run applications in containers. This guide will walk you through the steps to install Docker.io on a Linux system.

## Prerequisites

- A Linux-based operating system (e.g., Ubuntu, Debian, CentOS)
- A user account with `sudo` privileges

## Steps to Install Docker.io

1. **Update the package index:**

    Before installing Docker, update your package index to ensure you have the latest information about available packages.

    ```bash
    sudo apt-get update
    ```

2. **Install required packages:**

    Install the necessary packages to allow `apt` to use a repository over HTTPS.

    ```bash
    sudo apt-get install \
         apt-transport-https \
         ca-certificates \
         curl \
         software-properties-common
    ```

3. **Add Docker’s official GPG key:**

    Add Docker’s official GPG key to your system.

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4. **Set up the Docker repository:**

    Add the Docker repository to `apt` sources.

    ```bash
    sudo add-apt-repository \
         "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
         $(lsb_release -cs) \
         stable"
    ```

5. **Update the package index again:**

    After adding the Docker repository, update the package index again.

    ```bash
    sudo apt-get update
    ```

6. **Install Docker.io:**

    Install Docker from the Docker repository.

    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

7. **Manage Docker as a non-root user:**

    To avoid typing `sudo` whenever you run the `docker` command, add your user to the `docker` group.

    ```bash
    sudo groupadd -f docker && sudo usermod -aG docker $USER
    ```

    Log out and log back in so that your group membership is re-evaluated.

8. **Start the Docker service:**

    Start the Docker service if it is not already running.

    ```bash
    sudo system start docker
    ```

9. **Verify the Docker installation:**

    Verify that Docker is installed correctly by running the `hello-world` image.

    ```bash
    sudo docker run hello-world
    ```

    If Docker is installed correctly, you should see a message indicating that the installation was successful.

## Enable NVIDIA GPU Support

To enable NVIDIA GPU support in Docker, follow these steps:

1. **Install NVIDIA drivers:**

    Ensure that you have the appropriate NVIDIA drivers installed on your system. You can download the drivers from the NVIDIA website or install them using your package manager.

    ```bash
    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt-get install nvidia-driver-560
    ```

2. **Install NVIDIA Container Toolkit:**

    Install the NVIDIA Container Toolkit to enable GPU support in Docker.

    ```bash
    sudo curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    sudo curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    sudo apt-get update
    sudo apt-get install -y nvidia-docker2
    ```

3. **Configure Docker to use the NVIDIA runtime:**

    Configure Docker to use the NVIDIA runtime by default.

    ```bash
    sudo tee /etc/docker/daemon.json <<EOF
    {
         "default-runtime": "nvidia",
         "runtimes": {
              "nvidia": {
                    "path": "nvidia-container-runtime",
                    "runtimeArgs": []
              }
         }
    }
    EOF
    sudo systemctl restart docker
    ```

4. **Verify NVIDIA Docker installation:**

    Verify that the NVIDIA Docker installation is successful by running a test container.

    ```bash
    sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
    ```

    If the installation is successful, you should see the output of `nvidia-smi` showing the details of your GPU.

With these steps, you have enabled NVIDIA GPU support in Docker.

Congratulations! You have successfully installed Docker.io on your Linux system.
`