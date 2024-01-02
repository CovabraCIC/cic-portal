from flask import flash


def flash_form_errors(form, type: str = 'danger'):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{form[field].label.text}: {error}', f'{type}')