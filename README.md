# Настройка мультиязычности

### Логин и пароль к админке example

### Первый способ через библиотку parler в ветке parler:

1) Установка parler pip install django-parler

2) Добавить в settings 
   INSTALLED_APPS += (
       'parler',
   )
   
   LANGUAGES = [
       ('ru', _('Russian')),
       ('en', _('English')),
   ]
   
   LOCALE_PATHS = [
       os.path.join(BASE_DIR, 'название приложения/locale')
   ]
   
   Создвать папку locale в приложении и внутри создать папки с языками какие 
   указаны в settings.LANGUAGES
   
   PARLER_LANGUAGES = {
       None: (
           {'code': 'ru', },
           {'code': 'en', },
       ),
       'default': {
           'fallbacks': ['ru'],
           'hide_untranslated': False,
       }
   }

3) Добавить в корневой urls:
   urlpatterns = i18n_patterns(
       path('admin/', admin.site.urls),
       path('', include('change_language.urls')),
   )

4) Создавать модели с помощью parler.models

5) В шаблонах подргужать {% load i18n %} и в статичных данных использовать
   {% trans "Пример" %}
   Для получения текущего языка и перевобра всех языков использовать
   {% get_current_language as CURRENT_LANGUAGE %}
   {% get_available_languages as AVAILABLE_LANGUAGES %}
   {% get_language_info_list for AVAILABLE_LANGUAGES as languages %}

6) Для перевода страницы выполнить python manage.py makemessages --all, 
   переходим в папку locale и делаем перевод в файле либо через сторонее 
   приложение(Poedit) и использовать команду python manage.py compilemessages
   или через библиотеку rosetta установив ее pip install django-rosetta, 
   добавить в settings приложения и добавить в корневой url 
   path('rosetta/', include('rosetta.urls')), теперь можно делать переход 
   по url 127.0.0.1:8000/rosetta



### Второй способ через библиотку django-modeltranslation в ветке django-modeltranslation:

1) Установка pip install django-modeltranslation

2) Добавить в settings INSTALLED_APPS 'modeltranslation' и  установить языки 
   и путь к locale как в пункте 2 при установки parler

3) Создать файл translation.py в папке приложения и зарегестрировать каждую
   модель этого приожения которую нужно перевести

4) В admin.py зарегестрировать модель с помощью
   from modeltranslation.admin import TranslationAdmin, если не нужно
   показывать дубль оригинала + установленное поле с этим же языком

5) Сделать все миграции и ввести команду 
   python manage.py update_translation_fields для того чтобы все прошлые данные
   успешно перешли в поле языка по умолчанию и корректно отображались


## Лучший способ мне кажется через django-modeltranslation, т.к. не нужно 
## затрагивать модели и можно сделать миграции с полной бд
