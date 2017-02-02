# -*- coding: utf-8 -*-

import sys
from datetime import date, timedelta
from easyfile import read_yaml_file, write_csv_file
from profiles import get_project_params, unmarkdown_links


MAX_MONTH_DAYS = 32


def weekday_number(day_name):
    return [
        'mon', 'tue', 'wed',
        'thu', 'fri', 'sat', 'sun'
    ].index(day_name)


def usage():
    print 'Usage: schedule <recipe.yaml>'


def schedule_event(event_date, event_time, project):
    project_params = get_project_params(project)

    return {
        'Subject': '%s -- Morning Tsoding' % (project_params['title']),
        'Start date': event_date.strftime('%d/%m/%Y'),
        'Start time': event_time,
        'Description': unmarkdown_links(project_params['description'])
    }


def schedule_month(month, year, recipe):
    stream_week_days = set(map(weekday_number, recipe['days']))

    def is_stream_date(d):
        return (d.month == month) and (d.weekday() in stream_week_days)

    month_start = date(year, month, 1)
    stream_dates = filter(is_stream_date,
                          [month_start + timedelta(days=i)
                           for i in range(1, MAX_MONTH_DAYS)])

    return map(lambda (project, d): schedule_event(d, recipe['time'], project),
               zip(recipe['projects'] * MAX_MONTH_DAYS, stream_dates))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)

    recipe = read_yaml_file(sys.argv[1])
    today = date.today()
    write_csv_file('schedule.csv',
                   schedule_month(today.month, today.year, recipe))
