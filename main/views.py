from django.http import HttpResponse
from django.template import loader
import praw
import calendar
from utils import init_timestamp, add_days


def subreddit_home(request,year, subreddit):
    if request.method == 'GET':
        reddit_instance = praw.Reddit(
            client_id='dEJ9aEgYWjtELg',
            client_secret='li7VJglvPSpU9wg51Ive0sxFE-o',
            user_agent=str(
                'browser:reddit_history:v0.0.1 (by /u/reddit_history_guy)'
            )
        )
        subreddit_instance = reddit_instance.subreddit(subreddit)
        begin_timestamp = init_timestamp(year)
        lower = calendar.timegm(begin_timestamp.timetuple())
        upper = calendar.timegm(add_days(begin_timestamp).timetuple())
        search_query = 'timestamp:{0}..{1}'.format(
            lower, upper
        )
        search_results = subreddit_instance.search(
            query=search_query,
            sort='new'
        )

        template = loader.get_template('home.html')

        ret_context = {
            'subreddit': subreddit,
            'submissions': []
        }

        for result in search_results:
            subs = ret_context['submissions']
            subs.append({
                'title': result.title.encode('utf-8'),
                'permalink': result.permalink.encode('utf-8'),
                'ups': result.ups,
                'created_utc': result.created_utc,
                'num_comments': result.num_comments
            })

        return HttpResponse(
            template.render({"con": ret_context}, request)
        )


