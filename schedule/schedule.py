# -*- coding: utf-8 -*-

import sys
from datetime import date, timedelta
from easyfile import read_yaml_file, write_csv_file
from profiles import render_profile, get_project_params


MAX_MONTH_DAYS = 32


def weekday_number(day_name):
    return [
        'mon', 'tue', 'wed',
        'thu', 'fri', 'sat', 'sun'
    ].index(day_name)


def usage():
    print 'Usage: schedule <recipe.yaml> [months-forward]'


def schedule_event(event_date, event_time, project_name):
    project_params = get_project_params(project_name)

    return {
        'Subject': '%s -- Morning Tsoding' % (project_params['title']),
        'Start date': event_date.strftime('%d/%m/%Y'),
        'Start time': event_time,
        'Description': render_profile(project_name, 'Schedule', 'Unmarkdown')
    }


def schedule_month(month, year, recipe):
    stream_week_days = set(map(weekday_number, recipe['days']))

    def is_stream_date(d):
        return (d.month == month) and (d.weekday() in stream_week_days)

    month_start = date(year, month, 1)

    stream_dates = filter(is_stream_date,
                          [month_start + timedelta(days=i)
                           for i in range(MAX_MONTH_DAYS)])

    return map(lambda (project, d): schedule_event(d, recipe['time'], project),
               zip(recipe['projects'] * MAX_MONTH_DAYS, stream_dates))


def schedule_entry(recipe_filepath, output_filename, plus_months=0):
    recipe = read_yaml_file(recipe_filepath)
    today = date.today() + timedelta(weeks=plus_months * 4)
    schedule = schedule_month(today.month, today.year, recipe)
    write_csv_file(output_filename, schedule)
    return schedule


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(1)

    recipe_filepath = sys.argv[1]
    output_filename = 'schedule.csv'
    plus_months = 0
    if len(sys.argv) > 2:
        plus_months = int(sys.argv[2])

    schedule_entry(recipe_filepath, output_filename, plus_months)
    print 'Wrote to %s' % (output_filename)
