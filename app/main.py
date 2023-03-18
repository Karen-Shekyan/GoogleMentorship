from website import create_app

app = create_app()

if __name__ == "__main__": #used to execute the file
  app.run(debug=True)
