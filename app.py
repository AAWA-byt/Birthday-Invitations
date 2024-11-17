# main application file

from app import create_app

# Create the Flask app using the create_app function from the app module
app = create_app()

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=2683)
