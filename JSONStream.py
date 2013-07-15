
def JSONStream(fd, buffer_size=4096, decode=None):
	'''
	Decodes distinct JSON objects from a stream (a file-like object)
	Returns a generator that yields sequential JSON objects as they are retreived from the stream
	:param fd: A file-like object representing the input stream
	:param buffer_size: Optional read buffer size
	:param decode: An optional custom JSON decode function
	'''

	if not decode:
		import json
		decode = json.JSONDecoder().raw_decode
	buf = ''
	data = fd.read(buffer_size)
	while data:
		try:
			if not buf: data = data.lstrip()
			buf, data = buf+data, None
			while buf:
				obj, i= decode(buf)
				buf = buf[i:].lstrip()
				yield(obj)
		except GeneratorExit: break
		except ValueError: pass 
		if not fd.closed:
			data = fd.read(buffer_size)

