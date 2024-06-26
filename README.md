# Disease Classification Lab

1. This is an end-to-end deep learning pipeline designed to automatically detect coccidiosis in chicken fecal images. Coccidiosis is a common and economically significant disease affecting poultry, and early detection is crucial for effective management and treatment. This project utilizes state-of-the-art deep learning techniques to classify images as either healthy or affected by coccidiosis, achieving an impressive accuracy of 84%.

## Key Features

### Deep Learning Model
1. disease_classification_lab employs a deep learning model based on the VGG16 architecture, a widely-used convolutional neural network (CNN) pre-trained on the ImageNet dataset. This model serves as the backbone for image classification, with additional layers fine-tuned and optimized specifically for coccidiosis detection. Through extensive experimentation and parameter tuning, disease_classification_lab achieves superior performance in accurately identifying instances of coccidiosis.

### Scalable Infrastructure
To support the computational demands of training and inference, ChickSight leverages Amazon Elastic Compute Cloud (EC2) instances. These scalable virtual servers provide the necessary computational power for processing large volumes of image data efficiently. By utilizing EC2 instances, ChickSight ensures scalability and flexibility in handling varying workloads and dataset sizes.

### Secure Access Control
Security is a paramount concern when dealing with sensitive data such as poultry health information. disease_classification_lab implements Identity and Access Management (IAM) Users with granular permissions to manage access to resources within the AWS environment. This ensures that only authorized personnel have access to the trained model, dataset, and other project assets, maintaining the confidentiality and integrity of the data.

### Containerized Deployment
For seamless deployment across different environments, disease_classification_lab adopts a containerized approach using Docker. Containerization encapsulates the application and its dependencies into lightweight, portable containers, facilitating consistent deployment and execution across diverse computing environments. By containerizing disease_classification_lab, developers can easily deploy the application on local machines, cloud platforms, or hybrid environments without worrying about compatibility issues.

### Continuous Integration/Continuous Deployment (CI/CD)
disease_classification_lab embraces a DevOps approach with a robust CI/CD pipeline to automate the development, testing, and deployment processes. The pipeline incorporates tools such as Data Version Control (DVC), Flask, and Docker to ensure streamlined workflows from code changes to production deployment. With automated testing, validation, and deployment steps, disease_classification_lab accelerates the delivery of new features and updates while maintaining code quality and reliability.

## Getting Started

### Prerequisites
Before getting started with ChickSight, ensure you have the following prerequisites installed:

- Python (version 3.x)
- Docker
- AWS Account with access to EC2 and IAM services
- Git

### Installation
1. Clone the ChickSight repository to your local machine: </br>
` git clone https://github.com/KulkarniMihir/disease_classification_lab.git `

2. Create a conda environment after opening the repository </br>
` conda create -n disease_classification_lab python=3.8 -y ` </br>
` conda activate disease_classification_lab `

4. Install the required dependencies using pip: </br>
` pip install -r requirements.txt `

5. Finally run the following command </br>
` python app.py `

### AWS CICD Deployment with Github Actions

1. Login to AWS Console
2. Create IAM user for deployment:

   ` Access: ` </br> `1) EC2 access` </br> `2) ECR: Elastic Container registry to save your docker image in AWS`

   ` Policies: ` </br> `1) AmazonEC2ContainerRegistryFullAccess ` </br> `2) AmazonEC2FullAccess`
   
3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine
   Commands: </br>
   `sudo apt-get update -y` </br>
   `sudo apt-get upgrade` </br>
   `curl -fsSL https://get.docker.com -o get-docker.sh` </br>
   `sudo sh get-docker.sh` </br>
   `sudo usermod -aG docker ubuntu` </br>
   `newgrp docker` </br>
6. Configure EC2 as self-hosted runner: </br>
   `setting --> actions --> runner --> new self hosted runner --> choose os --> Run command one by one`
7. Setup Github Secrets: </br>
   `AWS_ACCESS_KEY_ID` </br>
   `AWS_SECRET_ACCESS_KEY` </br>
   `AWS_REGION` </br>
   `AWS_ECR_LOGIN_URI` </br>
   `ECR_REPOSITORY_NAME` </br>
   

### Usage
1. **Data Preparation**: Prepare your chicken fecal image dataset, ensuring it is properly labeled with corresponding health statuses (healthy or affected by coccidiosis).

2. **Training the Model**: Train the deep learning model using the provided scripts and configuration files. Experiment with hyperparameters and model architectures to optimize performance.

3. **Deployment**: Once trained, deploy ChickSight using the provided Dockerfile and deployment scripts. Configure AWS credentials and ensure proper setup for deployment on EC2 instances.

## Contributing
Contributions to ChickSight are welcome! Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions are valuable in advancing the project. To contribute, please follow these steps:

1. Fork the disease_classification_lab repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request detailing the changes you've made.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
I would like to express my gratitude to Krish Naik. YouTube video referred: [YouTube](https://youtu.be/p1bfK8ZJgkE?si=mNKMlHyyqRe7nmdx)
