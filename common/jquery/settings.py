from ragendja.settings_post import *
add_app_media(globals(), 'combined-%(LANGUAGE_CODE)s.js',
    'jquery/jquery.js',
    'jquery/jquery.fixes.js',
    'jquery/jquery.ajax-queue.js',
    'jquery/jquery.bgiframe.js',
    'jquery/jquery.livequery.js',
    'jquery/jquery.form.js',
)
