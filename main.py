import time

import pyupm_biss0001 as upmMotion
import pyupm_grove as grove
import pyupm_i2clcd as lcd

button = grove.GroveButton(8)
light = grove.GroveLight(0)
motion = upmMotion.BISS0001(3)
relay = grove.GroveRelay(2)
lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

while True:
    print 'Button value: ', button.value()
    print 'Light value: ', light.raw_value()
    print 'Motion value: ', motion.value()

    relay.on()

    lcd.setCursor(0,0)
    lcd.setColor(255, 0, 0)
    lcd.write('Hello World')

    time.sleep(1)

    relay.off()

del button
