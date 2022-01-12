# 장고 게시판
Django admin으로 만든 게시판

## 실행방법
1.원하는 경로에 해당 프로젝트를 깃 클론 받는다
```terminal
git clone https://github.com/lunayyko/django_admin_board.git
```

2.manage.py가 있는 디렉토리 상에 아래의 내용이 포함된 my_settings.py파일을 추가한다.
```python
SECRET_KEY = '랜덤한 특정 문자열'
```

3. 가상환경을 만들고 실행한다(미니콘다 설치 필요)
```bash
conda create -n cloudnine python=3.8
conda activate cloudnine
```

4. 라이브러리들을 설치한다
```python
pip install -r requirements.txt 
```

5. 유저를 생성한다
```python
python manage.py createsuperuser
```

6. 서버를 실행한다(파이썬 설치 필요)
```python
python manage.py runserver
```

7. localhost:8000/admin 화면으로 가서 로그인하고 게시글을 쓴다.

![Screen Shot 2022-01-12 at 5 48 38 PM](https://user-images.githubusercontent.com/8315252/149094355-c0d5cb53-aeb3-4e12-ab44-ca6be3f51de6.png)


8. 해당 화면에서 게시글의 생성, 조회, 수정, 삭제가 가능하다.

