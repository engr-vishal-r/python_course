def strip_whitespace(s): 
    return s.strip()
def to_lowercase(s): 
    return s.lower()
def remove_special_chars(s): 
    return ''.join(e for e in s if e.isalnum())

def compose(f, g): 
    return lambda x: f(g(x))

clean_text = compose(strip_whitespace, compose(to_lowercase, remove_special_chars))

print(clean_text("  Hello@World! "))
