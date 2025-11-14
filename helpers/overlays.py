# helpers/overlays.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def kill_overlays(driver, hard=True):
    driver.execute_script("""
    (function(){
      const sels = [
        'div[class*="Modal_modal_overlay"]',
        'div[class*="modal_overlay"]',
        'div[class*="overlay"]',
        'div[data-testid="modal"]',
        '#modals', '.modal'
      ];
      for (const sel of sels) {
        document.querySelectorAll(sel).forEach(e => { try { e.remove(); } catch(_){} });
      }
      %s
    })();
    """ % ("""
      Array.from(document.querySelectorAll('body *')).forEach(el=>{
        try{
          const st = getComputedStyle(el);
          const zi = parseInt(st.zIndex)||0;
          if (st.position==='fixed' && zi>=1000 && st.pointerEvents!=='none'
              && st.display!=='none' && st.visibility!=='hidden'
              && el.offsetWidth>0 && el.offsetHeight>0){
            el.parentElement && el.parentElement.removeChild(el);
          }
        }catch(_){}
      });
    """ if hard else ""))

def wait_no_overlay(driver, timeout=5):
    WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(
            By.CSS_SELECTOR,
            'div[class*="Modal_modal_overlay"], div[class*="modal_overlay"], div[class*="overlay"], div[data-testid="modal"]'
        )) == 0
    )
