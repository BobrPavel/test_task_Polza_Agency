import asyncio
import aiodns
from email_validator import validate_email, EmailNotValidError


async def check_mx(email, resolver):
    domain = email.split("@")[1]
    try:
        await resolver.query(domain, "MX")
        return f"{email} - домен валиден"
    except aiodns.error.DNSError as e:
        if e.args[0] == 4:  # NXDOMAIN — домен не существует
            return f"{email} - домен не существует"
        elif e.args[0] in (1, 3):  # NoAnswer — MX-запись отсутствует
            return f"{email} - MX-записи нет"
        else:
            return f"{email} - ошибка DNS: {e}"
    except Exception as e:
        return f"{email} - непредвиденная ошибка: {e}"


async def main():
    resolver = aiodns.DNSResolver()
    
    with open("Checking email domains 1\mails.txt", encoding="utf-8") as f:
        emails = [line.strip() for line in f if line.strip()]

    tasks = []
    for email in emails:
        # Проверка формата email
        try:
            validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            tasks.append(asyncio.create_task(asyncio.sleep(0, result=f"{email} - некорректный формат email")))
            continue
        
        tasks.append(asyncio.create_task(check_mx(email, resolver)))

    results = await asyncio.gather(*tasks)
    print("\n".join(results))


if __name__ == "__main__":
    asyncio.run(main())