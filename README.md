# My Python MVC App

This is a basic CRUD application built using the MVC (Model-View-Controller) architecture in Python. The application includes a login system and allows users to manage items.

## Project Structure

```
my-python-mvc-app
├── app
│   ├── controllers
│   │   ├── auth_controller.py
│   │   └── item_controller.py
│   ├── models
│   │   ├── user.py
│   │   └── item.py
│   ├── views
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   ├── login.html
│   │   │   ├── items_list.html
│   │   │   ├── item_detail.html
│   │   │   └── item_form.html
│   │   └── static
│   │       └── styles.css
│   └── __init__.py
├── tests
│   ├── test_auth.py
│   └── test_items.py
├── migrations
│   └── README.md
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

## Features

- User authentication (login/logout)
- CRUD operations for items
- Responsive web interface

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-python-mvc-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application settings in `config.py`.

## Usage

To run the application, execute the following command:
```
python main.py
```

Visit `http://localhost:5000` in your web browser to access the application.

## Testing

To run the tests, use:
```
pytest
```

## License

This project is licensed under the MIT License.