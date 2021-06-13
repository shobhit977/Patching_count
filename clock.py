from flask_apscheduler import APScheduler
from app import d_list,rem_title,rem_desc,rem_eid,mail,Message,app,t_list

scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()



@scheduler.task('cron',day=d_list[2],month=d_list[1],year=d_list[0],hour=t_list[0],minute=t_list[1])
def job1():
    with app.test_request_context():
        comm_email=['gmail.com','outlook.com','yahoo.com','hotmail.com','rediff.com']
        edomain=rem_eid.split('@')
        try:
            if edomain[1] not in comm_email:
                raise "email"
            msg = Message(subject = rem_title, body = rem_desc, sender = "anonymousanwitashobhit@outlook.com", recipients = [rem_eid])  
            mail.send(msg)
            app.logger.info('Mail sent')

        except:
            pass

