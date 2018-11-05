# Password Locker

This project aims at the task of saving passwords, and or generating them if the user isn't sure of his creativity.
## Prerequisites 

### You would need the following to work this app.

Working internet.

A terminal.

Python3.6.6 installed on your computer.

## Installing

Step 1: git clone https://github.com/Vynnel/Password-locker.git

Step 2: cd Password-locker

## Running the tests


### run this command lines in your terminal:
    
    chmod +x locker.py
    
    ./run.py


## Behavior Driven Development

The program should ask for user's username and password when ca(create account) is entered:

    Input Example: Enter ca

    Output Example: What is your username?

    Output Example: What is your password?

The program should authenticate the account by asking the user to login again when cc(create credential) is entered:

    Input Example: Enter cc

    Output Example: Login to your account. Username?

The program should create credentials when cc(create credential) is entered:

    Input Example: Enter cc

    Output Example: Enter the account name

The program should generate a random 8 characters long password when gp(generate password) is entered:

    Input Example: Enter gp

    Output Example: Your password is: kono3658baka

The program should let the user create their own password when cp(create password) is entered:

    Input Example: Enter cp

    Output Example: Enter your password

The program should display the credentials when dc(display credentials) is entered:

    Input Example: Enter dc

    Output Example: Here is a list of all of your credentials...

The program should end when ex(exit program) is entered:

    Input Example: Enter ex

    Output Example: Thank you for using Password locker...

## Built With

    Python3.6.6 - the language used.
    Visual Studio Code - the text editor.

## Authors

    Vynnel Omondi


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
## Acknowledgments

    Google
    Python
    Microsoft
    Github
