# Containers in Action: FinStack in Docker & Kubernetes

## Description
Containerize and orchestrate 3 buggy FinTech microservices:
- **Account Service**
- **Transaction Service**
- **Analytics Service**

Theme: Docker + Kubernetes + Helm

## Project Structure
```
finstack/
	service1/
		service.py
		controller.py
	service2/
		service.py
		controller.py
	service3/
		service.py
		controller.py
```

## How to Install
1. Ensure you have Python 3.8+ installed.
2. (Optional) Create a virtual environment:
	 ```powershell
	 python -m venv venv
	 .\venv\Scripts\activate
	 ```
3. Install dependencies (if any):
	 ```powershell
	 pip install -r requirements.txt
	 ```

## How to Run
Run any service controller directly, e.g.:
```powershell
python finstack/service1/controller.py
```

## How to Fix Bugs
Each service and controller contains intentional bugs. Here’s how to fix them:

### Account Service
- Check if `user_id` already exists before creating an account.
- Handle missing `user_id` in `get_balance`.
- Add input validation in controller.

### Transaction Service
- Validate `amount` before adding a transaction.
- Filter transactions by `user_id` in `get_transactions`.
- Add error handling in controller.

### Analytics Service
- Validate `value` before adding data.
- Handle empty data in `average` method.
- Add error handling in controller.

## Containerization & Orchestration
- Add Dockerfiles for each service.
- Use Kubernetes manifests and Helm charts for orchestration.

---
Feel free to explore, fix bugs, and containerize the services!
# BTech4thYear-Containers-in-Action-FinStack-in-Docker-Kubernetes