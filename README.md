# jcaroblog

### Environment
To replicate the environment run:
```
python -m venv /path/to/blog_env
pip install -r requirements.txt 
```
### Publishing ipynb
create a new notebook in jcaroblog/content/**new_notebook.ipynb**
be sure to include metadata in first cell:
```
- title: My notebook
- author: Jesus Caro
- date: 2023-05-11
- category: python
- tags: pip
```