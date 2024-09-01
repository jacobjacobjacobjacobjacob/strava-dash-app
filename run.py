# run.py
import main
from dashapp.app import app

if __name__ == "__main__":
    main.main()
    app.run_server(debug=True)
