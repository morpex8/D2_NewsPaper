
# (venv) PS D:\Проекты\Обучение\Python\Django\Newspaper> 
# py manage.py makemigrations
# py manage.py migrate
# py manage.py shell 
# from news.models import *
# user1 = User.objects.create(username='user1', first_name='Alex')
# Author.objects.create(authorUser=user1)
# user2 = User.objects.create(username='user2', first_name='Sergey')
# Author.objects.create(authorUser=user2)
# Category.objects.create(name='IT')
# Category.objects.create(name='Education')
# Category.objects.create(name='Different')
# Category.objects.create(name='New')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user1')), categoryType='NW', title='tratata title', text='tratata text')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user1')), categoryType='AR', title='tratatushki title', text='tratatushki text')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user2')), categoryType='NW', title='tratata2 title', text='tratata2 text')
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='user2')), categoryType='AR', title='tratatushki2 title', text='tratatushki2 text')
# p1 = Post.objects.get(pk=1)
# p2 = Post.objects.get(pk=2)
# p3 = Post.objects.get(pk=3)
# p4 = Post.objects.get(pk=4)
# c1 = Category.objects.get(name='IT')
# c2 = Category.objects.get(name='Education')
# c3 = Category.objects.get(name='Different')
# c4 = Category.objects.get(name='New')
# p1.postCategory.add(c1)
# p2.postCategory.add(c1, c2, c3, c4)
# p3.postCategory.add(c3, c2)
# p4.postCategory.add(c4)
# Comment.objects.create(commentUser=User.objects.get(username='user1'), commentPost = Post.objects.get(pk=1), text='comment text1')
# Comment.objects.create(commentUser=User.objects.get(username='user2'), commentPost = Post.objects.get(pk=1), text='comment text2')
# Comment.objects.create(commentUser=User.objects.get(username='user1'), commentPost = Post.objects.get(pk=2), text='comment text1')
# Comment.objects.create(commentUser=User.objects.get(username='user2'), commentPost = Post.objects.get(pk=3), text='comment text1')
# Comment.objects.create(commentUser=User.objects.get(username='user2'), commentPost = Post.objects.get(pk=4), text='comment text1')
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=3).like()
# Post.objects.get(pk=3).like()
# Post.objects.get(pk=4).dislike()
# Post.objects.get(pk=2).dislike()
# Post.objects.get(pk=1).dislike()
# Comment.objects.get(pk=1).like()
# Comment.objects.get(pk=1).like()
# Comment.objects.get(pk=1).dislike()
# Comment.objects.get(pk=2).like()
# Comment.objects.get(pk=2).like()
# Comment.objects.get(pk=2).like()
# Comment.objects.get(pk=2).dislike()
# Comment.objects.get(pk=3).like()
# Author.objects.get(authorUser = User.objects.get(username="user1")).update_rating()
# Author.objects.get(authorUser = User.objects.get(username="user2")).update_rating()
# a = Author.objects.get(authorUser = User.objects.get(username="user1"))
# b = Author.objects.get(authorUser = User.objects.get(username="user2"))
# a.ratingAuthor
# b.ratingAuthor
# Author.objects.get(authorUser = User.objects.get(username="user1")).ratingAuthor
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor') [0]
# print(best)



