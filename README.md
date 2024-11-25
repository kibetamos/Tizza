# Tizza - A Python Microservice Project

Welcome to Tizza, a Python microservice project designed to provide a lightweight and efficient service architecture. This project utilizes the principles of microservices to create scalable applications.
## Features
- Lightweight microservice architecture
- Scalable and maintainable codebase
- RESTful API for communication between services

## CI/CD Integration
Tizza incorporates CI/CD practices to automate testing and deployment, using GitHub Actions. This ensures that every change made to the codebase is automatically tested and validated.

The workflow is triggered on every push to the repository, ensuring that your code is consistently integrated and tested.

## Technologies Used

- Python
- Django
- Docker
- GitHub Actions for CI/CD

## Setup Instructions

Follow these steps to set up the project on your local machine:


1. **Clone the repository**:

   ```bash
   git clone https://github.com/kibetamos/Tizza.git
   cd Tizza

2. **Install the required dependencies**:
     Make sure you have Python and Django installed on your system. You can download the latest version from the official Python website here. After that, install the required packages:
   
      ```bash
   pip install -r requirements.txt
3. **Enable a virtual environment (optional but recommended):**
         ```bash
   python -m venv myenv
   source myenv/bin/activate  # On macOS/Linux
   myenv\Scripts\activate  # On Windows


### Running the Project
To run the project, execute the following command in your terminal:
      ```bash
         python manage.py runserver
         
### Accessing the Service

Once the project is running, you can access it in your web browser by navigating to:

```bash
http://127.0.0.1:8000

