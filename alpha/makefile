run:
	uv run uvicorn app.main:app --reload

clean:
	rm -rf __pycache__ *.pyc *.pyo .pytest_cache .mypy_cache
	rm -rf app/__pycache__ 
	rm -rf app/database/__pycache__ 
	rm -rf app/services/__pycache__ 
	rm -rf app/models/__pycache__
	rm -rf models/__pycache__ 