import webbrowser

user_term =input("Enter a search name: ").replace(' ', '+')

#webbrowser.open("https://google.com")

webbrowser.open("https://www.google.com/search?q="+user_term)

