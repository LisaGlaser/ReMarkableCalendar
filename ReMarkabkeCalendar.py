#!/usr/bin/env python

import calendar
import os
import sys

## add desired output folder here
path='/home/glaser/Documents/CalenderTemplate/ReMarkableCalendar'

#generate preamble
def write_preamble(f):
    ## Morning starttime
    starttime="8"
    ## Evening time
    stoptime="21"
    ## Starttime sunday
    # Min \starttime+1
    # Max \stoptime-2
    sundaybegin="14"
    ## Rule width thick
    thickrulewidth="2pt"
    ## Midrule width
    midrulewidth="1pt"
    ## Thinrule width
    thinrulewidth=".5pt"

    ## Exta space
    extrarowheight="1pt"


    f.write(r'\documentclass[fontsize=6pt]{scrartcl}'+'\n')
    f.write(r'\usepackage[paperheight=187.2mm,paperwidth=140.4mm,tmargin=20pt, lmargin=1pt, rmargin=3pt, bmargin=0pt]{geometry}'+'\n')
    f.write(r'\usepackage{tabularx,booktabs,multirow}'+'\n')
    f.write(r'\usepackage{calendar} % Use the calendar.sty style'+'\n')
    f.write(r'\usepackage{palatino} % Use the Palatino font'+'\n')
    f.write(r'\usepackage[OT1]{fontenc}'+'\n')
    f.write(r'\usepackage[colorlinks=true]{hyperref}'+'\n')
    f.write(r'\begin{document} '+'\n')
    f.write(r'\pagestyle{empty} % Disable default headers and footers'+'\n')
    f.write(r'\setlength{\parindent}{0pt} % Stop paragraph indentation'+'\n')
    f.write(r'\StartingDayNumber=2 % The starting day of the calendar, default of 1 means Sunday, 2 for Monday, etc'+'\n')
    f.write(r'\newcount\counter'+'\n')
    f.write(r'\newcount\startdate'+'\n')
    f.write(r'\newcount\starttime'+'\n')
    f.write(r'\newcount\stoptime'+'\n')
    f.write(r'\newcount\sundaybegin'+'\n')
    f.write(r'\newcount\week'+'\n')
    f.write(r'\newcount\datemonday'+'\n')
    f.write(r'\newcount\datetuesday'+'\n')
    f.write(r'\newcount\datewednesday'+'\n')
    f.write(r'\newcount\datethursday'+'\n')
    f.write(r'\newcount\datefriday'+'\n')
    f.write(r'\newcount\datesaturday'+'\n')
    f.write(r'\newcount\datesunday'+'\n')
    #   %% Morning starttime
    f.write(r'\starttime='+str(starttime)+'\n')
    #%% Evening time
    f.write(r'\stoptime='+str(stoptime)+'\n')
    #%% Starttime sunday
    f.write(r'\sundaybegin='+str(sundaybegin)+'\n')
    f.write(r'   %% Rule width thick'+'\n')
    f.write(r'   \newcommand{\rulew}{'+str(thickrulewidth)+r'}'+'\n')
    f.write(r'   %% Midrule width'+'\n')
    f.write(r'   \newcommand{\mrulew}{'+str(midrulewidth)+r'}'+'\n')
    f.write(r'   %% thinrule width'+'\n')
    f.write(r'   \newcommand{\trulew}{'+str(thinrulewidth)+r'}'+'\n')
    f.write(r'   %% Extra space'+'\n')
    f.write(r'   \setlength{\extrarowheight}{'+str(extrarowheight)+r'}'+'\n')
    f.write(r'   %'+'\n')
    f.write(r'   %%%%%%%%%% DEFINITIONS %%%%%%%%%%'+'\n')
    f.write(r'   %'+'\n')

    f.write(r'\newcommand{\lendt}{\cmidrule[\rulew](l){1-2}\cmidrule[\rulew](l){3-4}\cmidrule[\rulew](l){5-6}\cmidrule[\rulew](l){7-8}\cmidrule[\rulew](l){9-10}\cmidrule[\rulew](l){11-12}}'+'\n')
    f.write(r'\newcommand{\lend}{\cmidrule(l){1-2}\cmidrule(l){3-4}\cmidrule(l){5-6}\cmidrule(l){7-8}\cmidrule(l){9-10}\cmidrule(l){11-12}}'+'\n')
    f.write(r'\newcommand{\lsun}{\cmidrule(l){1-2}\cmidrule(l){3-4}\cmidrule(l){5-6}\cmidrule(l){7-8}\cmidrule(l){9-10}}'+'\n')
    f.write(r'\newcommand{\lsunt}{\cmidrule(l){1-2}\cmidrule(l){3-4}\cmidrule(l){5-6}\cmidrule(l){7-8}\cmidrule(l){9-10}\cmidrule[\rulew](l){11-12}}'+'\n')
    f.write(r'\newcommand{\printday}[2]{{\huge \textbf{#1}}\,\, \LARGE \textbf{#2}}'+'\n')
    f.write(r'\newcommand{\neutralline}{& & & & & & && & &}'+'\n')
    f.write(r'\newcommand{\footer}{\centering\rule{12cm}{\cmidrulewidth} \raisebox{-0.5ex}{\LaTeX{}} \rule{7cm}{\cmidrulewidth}}'+'\n')
    f.write(r'\newcommand{\printmonthleft}{{\LARGE \textbf{pymonthleft}}}'+'\n')
    f.write(r'\newcommand{\printmonthright}{{\LARGE \textbf{pymonthright}}}'+'\n')
    f.write(r'  %'+'\n')
    f.write(r' \advance\stoptime1'+'\n')
    return "wrote preamble"


#generate the months pages
def gen_months(year,f):
    week=0
    cal=calendar.Calendar()
    for month_number in range(1,13):
        monthname=str(calendar.month_name[month_number])
        month=cal.itermonthdays(year,month_number)#month is an iterable generator

        f.write(r'\begin{center}'+'\n')
        f.write(r'\hypertarget{mon:'+str(monthname)+r'}{\textbf{\LARGE '+str(monthname)+r'}}'+'\n')
        f.write(r'\textbf{\LARGE %s}' %(str(year))+'\n')
        f.write(r'\end{center}'+'\n')
        f.write(r'\begin{calendar}{\textwidth} '+'\n')

        # blankdays=calendar.weekday(year,month_number,1)%7
        # for blank in range(blankdays):
        #     f.write(r'\BlankDay' +'\n')

        lastblank=False
        firstblank=True
        for i in month:
            print(monthname,i)
            if(i==0):
                if(firstblank): ## loop prepared to have week number also in the truncated week, but can't make it work w. calendar.sty right now
                    f.write(r'\BlankDay' +'\n')
                    firstblank=False
                    lastblank=True
                else:
                    f.write(r'\BlankDay' +'\n')
                    lastblank=True

            else:
                if lastblank:
                    f.write(r'\setcounter{calendardate}{1} % Start the date counter at 1'+'\n')
                    lastblank=False
                if calendar.weekday(year,month_number,i)==0:
                    week+=1
                    f.write(r'\day{ \hyperlink{week'+str(week)+r'}{W'+str(week)+r'}}{\vspace{1.7cm}} % '+str(i) +'\n')
                else:
                    f.write(r'\day{}{\vspace{1.7cm}} % '+str(i) +'\n')

        f.write(r'\finishCalendar{}' +'\n')
        f.write(r'\end{calendar}' +'\n')
    #    f.write(r'\footer'+'\n')
        f.write(r'\newpage'+'\n')
    return "write months"

#generate the weeks pages
def gen_weeks(year,f):
    months = [calendar.LocaleTextCalendar().formatmonthname(year,i,1).split(' ')[0] for i in range(1,13)]
    labels = {
        'label_week':       'Week',
        'label_monday':     'Mon',
        'label_tuesday':    'Tue',
        'label_wednesday':  'Wed',
        'label_thursday':   'Thu',
        'label_friday':     'Fri',
        'label_saturday':   'Sat',
        'label_sunday':     'Sun',
    }
    days = {
        0: 'pymond',
        1: 'pytue',
        2: 'pywed',
        3: 'pythur',
        4: 'pyfr',
        5: 'pysat',
        6: 'pysun'
    }

    #Collect all mondays in a list
    mondays = []

    for month in range( 1, 13 ):

       for week in calendar.monthcalendar(year,month):

          if not week[0] == 0:
             mondays.append( [week[0], 0] )

    # If year doesn't end with a friday, append January to months
    if calendar.monthcalendar(year, 12)[-1][-1] == 0:
        months.append( months[0] )

    Nweeks = len(mondays)

    # Add length of corresponding month to each monday
    month = 1
    for week in range( Nweeks ):

       Ndaysinmonth = calendar.monthrange( year, month )[1]

       # First week
       if week == 0:
          mondays[week][1] = Ndaysinmonth

       # Increasing day in month => same month
       elif mondays[week][0] > mondays[week-1][0]:
          mondays[week][1] = Ndaysinmonth

       # Next month
       else:
          mondays[week][1] = calendar.monthrange( year, month+1 )[1]
          month+=1

    table = r'''
       %% Weeknumber
       \week=pyweek
       \renewcommand{\printmonthleft}{{\LARGE \hyperlink{mon:pymonthleft}{\textbf{pymonthleft}}} }
       \renewcommand{\printmonthright}{{\LARGE \hyperlink{mon:pymonthright}{\textbf{pymonthright}}} }
        %% Dates
       \datemonday=pymond
       \datetuesday=pytue
       \datewednesday=pywed
       \datethursday=pythur
       \datefriday=pyfr
       \datesaturday=pysat
       \datesunday=pysun
       %
       %

       \long\def\addto#1#2{\expandafter\def\expandafter#1\expandafter{#1#2}}

       %
       %%%%%%%%%% TABLE CONTENT RIGHT SIDE %%%%%%%%%%
       %
       \def\tabledatarightupper{} \counter=\the\starttime
       \loop
          \edef\tabline{\the\counter &  & \the\counter & &\the\counter  &  & \the\counter & &\the\counter  &  & }
          \expandafter\addto\expandafter\tabledatarightupper\expandafter{\neutralline \\\lend}
          \expandafter\addto\expandafter\tabledatarightupper\expandafter{\tabline \\\lend}
          \advance \counter 1
          \ifnum \counter<\the\sundaybegin
       \repeat
       %
       \advance\sundaybegin1
       \def\tabledatarightinter{} \counter=\the\sundaybegin
       \newcount\sundaystop
       \sundaystop=\the\sundaybegin
       \advance\sundaystop1
       \loop
            \edef\tabline{\the\counter &  & \the\counter & & \the\counter & & \the\counter & &\the\counter & &}
          \expandafter\addto\expandafter\tabledatarightinter\expandafter{\neutralline \\\lsun}
          \expandafter\addto\expandafter\tabledatarightinter\expandafter{\tabline \\\lsun}
          \advance \counter 1
          \ifnum \counter<\the\sundaystop
       \repeat
       \advance\sundaybegin-1
       \advance\sundaystop1
       %
       \def\tabledatarightlower{} \counter=\the\sundaystop
       \loop
         \edef\tabline{\the\counter &  & \the\counter & & \the\counter & & \the\counter & &\the\counter & &}
          \expandafter\addto\expandafter\tabledatarightlower\expandafter{\neutralline \\\lend}
          \expandafter\addto\expandafter\tabledatarightlower\expandafter{\tabline \\\lend}
          \advance \counter 1
          \ifnum \counter<\the\stoptime
       \repeat
       \advance\sundaystop-1
       %
       \pagestyle{empty}

       %
       %%%%%%%%%% RIGHT TABLE %%%%%%%%%%
       %
       \noindent
    \begin{tabularx}{\linewidth}{lXlXlXlXlXlXlX}
          \multicolumn{12}{l}{{\hypertarget{weekpyweek}{\LARGE Week \the\week} }\hfill \printmonthright}\\[.2em]\midrule[\rulew]
          \multicolumn{2}{l}{\printday{\the\datemonday}{label_monday}}  &%
          \multicolumn{2}{l}{\printday{\the\datetuesday}{label_tuesday}}  &%
          \multicolumn{2}{l}{\printday{\the\datewednesday}{label_wednesday}}  &%
          \multicolumn{2}{l}{\printday{\the\datethursday}{label_thursday}}  &%
          \multicolumn{2}{l}{\printday{\the\datefriday}{label_friday}}     &%
          \multicolumn{2}{l}{\printday{\the\datesaturday}{label_saturday}}  \\[0.5cm]
          & & & & & & & & & & \\\lendt
          \tabledatarightupper
          & & & & & & & & & & \\\lsunt
          \the\sundaybegin & & \the\sundaybegin & &\the\sundaybegin & & \the\sundaybegin & &\the\sundaybegin & & \multicolumn{2}{l}{\multirow{4}{*}[1.5em]{\printday{\the\datesunday}{label_sunday}}}\\\lsun
          \tabledatarightinter
          & & & & & & & & & & \\\lsun
          \the\sundaystop & & \the\sundaystop & & \the\sundaystop & & \the\sundaystop & & \the\sundaystop & &  & \\\lsunt
          \tabledatarightlower
          & & & & & & & & & & \\\lendt
       \end{tabularx}
       %
       \vfill
       %\footer
       \clearpage'''

    for key in labels:
        table = table.replace(key, labels[key])
    week_label = 0

    if mondays[0][0] != 1:
        week_label += 1

    currentmonth = 0
    for week in range(Nweeks):

       table_temp = table
       trigger = 0

       for weekday in range(7):

          date = mondays[week][0] + weekday

          # If it's monday 1 st, increase currentmonth unless it's January 1 st.
          if date == 1 and not (mondays[0][0] == 1 and currentmonth == 0):
             currentmonth += 1
             trigger = 1

          # If next month
          if date > mondays[week][1]:

             date = date - mondays[week][1]

             if trigger == 0:
                currentmonth += 1
                trigger = 1

             # Print right page
             if weekday > 2:
                table_temp = table_temp.replace('pymonthright', months[currentmonth])

             # Print left page
             else:
                table_temp = table_temp.replace('pymonthleft', months[currentmonth])

          else:

             # Print left page
             if weekday == 2:
                table_temp = table_temp.replace('pymonthleft', months[currentmonth])

             # Print right page
             elif weekday == 6:
                table_temp = table_temp.replace('pymonthright', months[currentmonth])

          table_temp = table_temp.replace(days[weekday], str(date))

       table_temp = table_temp.replace("pyweek", str(week_label))
       f.write(table_temp)
       week_label += 1

    return "write weeks"



#finish the calendar
def finish_calendar(f):
    f.write(r'\end{document}' +'\n')
    return "finished the file"

#spit it out together

def perfect_calendar(year, months=True,weeks=True,StandardFilename=True):
    if(months==False and weeks==False):
        print("We can only make monthly or weekly calendars for now, without either there is no calendar.")
        return "Sorry, not sorry."
    if StandardFilename:
        StandardFilename=path+'/'+str(year)+'.tex'
    print("File is named {}".format(StandardFilename))
    ## open tex file
    with open(StandardFilename,'w') as file:
        print(write_preamble(file))
        if(months):
            print(gen_months(year,file))
        if(weeks):
            print(gen_weeks(year,file))
        print(finish_calendar(file))
    os.system('pdflatex {}'.format(StandardFilename))

    return "done"


if __name__ == "__main__":
    print("Which year would you like a calendar for?")
    year = int(input())
    print("If you want more customisation, please edit the script.")
    perfect_calendar(year)
