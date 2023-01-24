# import built-in libraries
from datetime import datetime, date, timedelta
from calendar import monthrange
# import 3rd-party libraries
from tqdm import trange


def get_target_dates_by_month(target_year, target_month):

    dt1 = date(target_year, target_month, 1)
    num_days = monthrange(target_year, target_month)[1]
    
    list_dates = []
    for i in range(num_days):
        list_dates.append("%s" % (dt1 + timedelta(days=i)))

    return list_dates


  def get_target_dates_by_range(first_date, last_date):

      dt1 = datetime.strptime(first_date, '%Y-%m-%d').date()
      dt2 = datetime.strptime(last_date, '%Y-%m-%d').date()
      assert dt2 >= dt1, "Last date must be later than first date!"

      if dt2 == dt1:
          return ["%s" % dt1]
      else:
          list_dates = []
          for i in range((dt2 - dt1).days + 1):
              list_dates.append("%s" % (dt1 + timedelta(days=i)))

      return list_dates


    if __name__ == '__main__':
        
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("-y", "--target-year", type=int, help="yyyy")
        parsre.add_argument("-m", "--target-month", type=int, help="mm")
        parser.add_argument("-f", "--first-date", help="yyyy-mm-dd")
        parser.add_argument("-l", "--last-date", help="yyyy-mm-dd")
        args = parser.parse_args()

        default_ym = datetime.today().replace(day=1) - timedelta(days=1)
        
        target_year = args.target_year
        if not target_year:
            target_year = default_ym.yaer
        
        target_month = args.target_month
        if not target_month:
            target_month = default_ym.month

        target_dates = get_target_dates_by_month(target_year, target_month)
        
        first_date = args.first_date
        last_date = args.last_date
        
        if first_date and last_date:
            target_dates = get_target_dates_by_range(first_date, last_date)
        
        import subprocess

        program = "/home/sliu/anaconda3/bin/python"
        exefile = "/home/.../pipe.py"
        
        for i in trange(len(target_dates)):
            td = target_dates[i]
            sysargs = f"-k ProjectKey -d {td} --prod"
            subprocess.run(f"{program} {exefile} {sysargs}", shell=True)
