# Правила написания кода

## IDE
В git проекта сознательно закладываются настройки IDE (дир-я .idea.example).
В ней лежат настройки ide, соответствующие установленному code-style. 
В частности настройки длины строки и обновленный словарь с переменными.

Это может выглядеть избыточной педантичностью, но нет. Это инвестиция в 
легкость долгосрочной поддержки проекта. Ее не хватает 95% проектов, 
с которыми я сталкивался.

## Правила code-style
- Любая длина строки < 100 символов. Это стандартная ширина ubuntu-терминала, 
  когда он развернут на пол экрана. 
- В проекте не должно быть предупреждений pycharm-professional, кроме 
  "замалчиваемых явно" (python zen). 
  - Проверить предупреждения во всем проекте можно в ide "code"->
    "inspect code style". Рекомендуется настроить проверяемые директории
    и не включать туда .idea, .idea.example.
  - Раз в N времени проводится проверка в результате которой проблемные участки
    или помечаются комментариями (может быть с TODO), или добавляются
    в замалчивание (с последующим обновлением .idea.example), или исправляются.