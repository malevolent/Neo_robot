#!/usr/bin/env python
# coding: utf-8
# Author: Vincent FOUCAULT
# Here is a text-to-speech wrapper for Espeak
# It's part of QBO robot ros softwares


import rospy
from qbo_talk.srv import Text2Speach # read service content (words we want to be spoken)
import os

# Some possibilities of different languages
fr1_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-fr1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/fr1 - -.au | paplay"
en1_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-en1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/en1 - -.au | paplay"

class talk():

    def __init__(self):

        rospy.init_node('talk', anonymous=True)
        fr1 = rospy.Service('say_fr1', Text2Speach, self.fr1_talk)
        en1 = rospy.Service('say_en1', Text2Speach, self.en1_talk)

    def fr1_talk(self, speak):
        os.system(fr1_speak % speak.sentence)
        return []

    def en1_talk(self, speak):
        os.system(en1_speak % speak.sentence)
        return []

if __name__ == '__main__':
    try:
        talk = talk()
        rospy.spin()
    except rospy.ROSInterruptException: pass

