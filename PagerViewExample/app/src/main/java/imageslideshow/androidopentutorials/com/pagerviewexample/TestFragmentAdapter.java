package imageslideshow.androidopentutorials.com.pagerviewexample;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

import com.viewpagerindicator.IconPagerAdapter;

import java.util.ArrayList;

/**
 * Created by nanenare on 5/22/16.
 */
public class TestFragmentAdapter extends FragmentPagerAdapter {


    private  static final Integer[] drawableImage = {R.drawable.vanadzor_1, R.drawable.vanadzor_2, R.drawable.vanadzor_3, R.drawable.vanadzor_4};

    protected static final int[] ICONS = new int[] {
    };

    private int mCount = drawableImage.length;

    public TestFragmentAdapter(FragmentManager fm) {
        super(fm);

    }

    @Override
    public Fragment getItem(int position) {
        return TestFragment.newInstance(drawableImage[position % drawableImage.length]);
    }

    @Override
    public int getCount() {
        return mCount;
    }

//    @Override
//    public CharSequence getPageTitle(int position) {
//        return TestFragmentAdapter.CONTENT[position % CONTENT.length];
//    }

//    @Override
//    public int getIconResId(int index) {
//        return ICONS[index % ICONS.length];
//    }

    public void setCount(int count) {
        if (count > 0 && count <= 10) {
            mCount = count;
            notifyDataSetChanged();
        }
    }
}