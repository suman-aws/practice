import os

def update_secrets():
    with open('test1.template.yaml', 'r') as file:
        template = file.read()

    secrets = {
        'iam_name': os.getenv('iam_name'),
        'iam_pass': os.getenv('iam_pass'),
        'db_name': os.getenv('db_name'),
        'db_pass': os.getenv('db_pass'),
    }

    for key, value in secrets.items():
        template = template.replace(f'{{{{{key}}}}}', value)

    with open('test1.yaml', 'w') as file:
        file.write(template)

if __name__ == "__main__":
    update_secrets()
