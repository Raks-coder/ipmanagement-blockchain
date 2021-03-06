# --------------------------------------- START OF LICENSE NOTICE ------------------------------------------------------
# Copyright (c) 2018 Soroco Private Limited. All rights reserved.
#
# NO WARRANTY. THE PRODUCT IS PROVIDED BY SOROCO "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL SOROCO BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
# ---------------------------------------- END OF LICENSE NOTICE -------------------------------------------------------
#
#   Primary Author: Shivam Vijaywargiya <shivam.vijaywargiya@soroco.com>
#
#   Purpose: A short description of the purpose of this source file ...

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False