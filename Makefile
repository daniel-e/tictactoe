all:
	tar xzf extra/nginx-1.10.3.tar.gz
	cd nginx-1.10.3/ && ./configure --prefix=/opt/nginx && make -j4 && make install
	rm -rf nginx-1.10.3/
	cp extra/nginx.conf /opt/nginx/conf/
	mkdir /opt/nginx/tictactoe
	cp html/* /opt/nginx/tictactoe/
