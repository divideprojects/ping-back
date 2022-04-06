test:
	@pre-commit run --all-files

run:
	@uvicorn app:app --reload

clean:
	@pyclean app/
