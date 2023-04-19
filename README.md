# xsd2xml
A Python module that generates XML matching an XSD and (optionally) regex constraints for the value of each tag.

## Usage

```bash
python -m xsd2xml
```

## Contstraints

The "key feature" in this package that I couldn't find in any other xml generator is the ability to generate data matching certain constraints. That could be telephone numbers, e-mail addresses, dates, or just random numbers within a range. This enables you to generate more meaningful data within your domain.

Format your constraints as Python regular expressions, and store them within a TOML file. For example:

```toml
[constraints]

# XPath = Regex
email = '^\S+@\S+\.\S+$'
"fruit/apple" = "golden_delicious|honey_crisp"
```
