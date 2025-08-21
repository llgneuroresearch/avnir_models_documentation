# CT Brain Extraction

The CT Brain Extraction tool (CTbet) is a powerful utility designed to efficiently extract brain regions from CT images using a Docker container.

## Prerequisites

Before using CTbet, ensure the following:

- Docker is installed on your system. Refer to the [Docker Installation Guide](../docker.md) or the [official Docker documentation](https://docs.docker.com/get-docker/) for setup instructions.
- Your system meets the hardware requirements for running Docker containers, especially if you plan to use GPU acceleration.

> **Important**: If you want to run the inference using CUDA, please use NVIDIA driver 560 or higher and CUDA 12.6 or higher.

## Installation

To install CTbet, pull the Docker image from the repository:

```bash
docker pull llgneuroresearch/ctbet:1.0.0
```

## Usage

To run the inference, run the following command:

    ```bash
    docker run -ti -v /path/to/your/data:/input -v /path/to/your/output:/output \
    -u 0:$(id -g) --gpus all --rm --shm-size 2g avnirlab/ctbet:1.0.0 -device cuda
    ```
    
    - Replace `/path/to/your/data` with the directory containing your input CT images.
    - Replace `/path/to/your/output` with the directory where you want the output files to be saved.
    - Use the `-device cuda` flag for GPU-based inference. For CPU-based inference, replace `cuda` with `cpu` and remove `--gpus all` flag.

## Example Workflow

Here’s a step-by-step example to demonstrate CTbet usage:

1. **Prepare directories**:

    ```bash
    mkdir output_directory
    ls input_data/
    > image1.nii.gz  image2.nii.gz
    ```

2. **Run CTbet**:

    ```bash
    docker run -ti -v $(pwd)/input_data:/input -v $(pwd)/output_directory:/output \
    -u 0:$(id -g) --gpus all --rm --shm-size 2g avnirlab/ctbet:latest -device cuda
    ```

3. **Check the output**:

    ```bash
    ls output_directory/results
    > image1.nii.gz image2.nii.gz dataset.json plans.json predict_from_raw_data_args.json
    ```

    In the output_directory, the Nifti images are the predicted brain extraction masks.

## Additional Resources

- **GitHub Repository**: [CTbet-Docker](https://github.com/llgneuroresearch/CTbet-Docker)
- **Docker Documentation**: [Get Started with Docker](https://docs.docker.com/get-started/)