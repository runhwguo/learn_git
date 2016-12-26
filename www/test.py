import asyncio
import sys

from www import orm
from www.models import User


async def test():
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test()]))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
