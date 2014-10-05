#!/usr/bin/env python

import sys
sys.path.insert(0, '../..')

from app import app
app.run(host='0.0.0.0', port=80, debug=True)
