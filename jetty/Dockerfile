FROM jetty

WORKDIR $JETTY_BASE
CMD java -jar $JETTY_HOME/start.
COPY sample.war /var/lib/jetty/webapps/sample.war
EXPOSE 8080
